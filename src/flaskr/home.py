from flask_wtf import FlaskForm
from wtforms import BooleanField, SubmitField, FileField, IntegerField, SelectField, StringField, RadioField
from sensors import Prediction, Cleanser

from DataGeneration import DataGeneration
from DataUpload import DataUpload

from flask import flash

class HomeForm(FlaskForm):
    channel_id = IntegerField('Channel ID')
    field_id = IntegerField('Field ID')
    start_date = StringField('Start Date')
    time_increment = IntegerField('Time Increment')  # Modify choices as needed
    cleanse = BooleanField('Cleanse Data')
    predict = BooleanField('Predict Data')
    prediction_date = StringField('Prediction Date')
    chartType = SelectField('Chart Type', choices=[('line', 'bar', 'radio')])  # Modify choices as needed
    stdDeviation = IntegerField('Standard Deviation')
    file = FileField('File Upload')

    

    def conflicting_input(self):
        api_query_is_provided = self.channel_id.data and self.field_id.data and self.start_date.data and self.time_increment.data
        upload_data_is_provided = bool(self.file.data)

        if (api_query_is_provided and upload_data_is_provided) or (not api_query_is_provided and not upload_data_is_provided):
            return True
        
        return False
    
    def conflicting_modifers(self):
        if not self.cleanse.data and self.predict.data:
            return True

        return False

    def get_time_series_data(self):


        if (self.file.data is not None) and (self.file.data.filename != ''):
            try:
                data_gen = DataUpload(self.file.data)
                date_series, value_series = data_gen.get_time_series()

            except Exception as e:
                flash(f"Error while generating data: {e}")
        
        else:
            # Initialize DataGeneration with form data
            try:

                data_gen = DataGeneration(self.channel_id.data, self.time_increment.data, self.field_id.data, self.start_date.data)
                date_series, value_series = data_gen.get_time_series()

            except Exception as e:
                flash(f"Error while generating data: {e}")  # Use flash for error messages

        return date_series, value_series

    def apply_data_modifiers(self, sensor):
        if self.cleanse.data:
            sensor = Cleanser.cleanser(sensor, deviations=self.stdDeviation.data)

        if self.predict.data:
            sensor = Prediction.DataPrediction(sensor, self.prediction_date.data)

        labels, values = sensor.process_data()
        sensor.set_date_range(labels)
        sensor.set_value(values)

        return sensor
    
class AlarmForm(FlaskForm):
    alarm_min = IntegerField('Alarm Minimum Trigger')
    alarm_max = IntegerField('Alarm Maximum Trigger')
    highlow = RadioField('Trigger Region', choices=[(1,'Higher'),(-1,'Lower')], default='1')
    submit = SubmitField('Submit')
    
    
