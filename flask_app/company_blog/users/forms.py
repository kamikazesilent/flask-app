from flask_wtf import FlaskForm
from wtforms import ValidationError, StringField, PasswordField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, Email,EqualTo
from company_blog.models import User
from flask_wtf.file import FileField, FileAllowed

class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(),Email() ]) 
    Password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('ログイン')

class RegistrationForm(FlaskForm):
    email = StringField('メールアドレス', validators=[DataRequired(), Email(message='正しいメールアドレスを入力してください') ])
    username = StringField('ユーザー名',validators=[DataRequired()])
    Password = PasswordField('パスワード',validators=[DataRequired(), EqualTo('Pass_confirm',message='パスワードが一致していません')])
    Pass_confirm = PasswordField('パスワード（確認)',validators=[DataRequired()])
    submit = SubmitField('登録')

    def validate_username(self, field):
        if User.query.filter_by(username=field.data).first():
            raise ValidationError('入力されたユーザー名は既に使われています。')
    
    def validate_email(self, field):
        if User.query.filter_by(email=field.data).first():
            raise ValidationError('入力されたメールアドレスは既に登場されています。')
    
class UpdateUserForm(FlaskForm):
    email = StringField('メールアドレス', validators=[DataRequired(),Email(message="正しいメールアドレスを入力してください")])
    username = StringField('ユーザー名', validators=[DataRequired()])
    Password = PasswordField('パスワード', validators=[EqualTo('Password_confirm', message='パスワードが一致していません。')])                                                                                                                                                                                                               
    Password_confirm = PasswordField('パスワード確認')
    submit =SubmitField('更新')

    def __init__(self, user_id, *args, **kwargs):
        super(UpdateUserForm, self).__init__(*args, **kwargs )
        self.id = user_id  
    
    def validate_email(self, field):
        if User.query.filter(User.id != self.id).filter_by(email=field.data).first():                                                 
            raise ValidationError('入力されたメールアドレスは既に登録されています。')
        
    def validate_username(self, field):
        if User.query.filter(User.id != self.id).filter_by(username=field.data).first():                                           
            raise ValidationError('入力されたユーザー名は既に使われています。')

class InquiryForm(FlaskForm):
    name = StringField('お名前(必須)',validators=[DataRequired()])
    email = StringField('メールアドレス(必須)',validators=[DataRequired(),Email(message='正しいメールアドレスを入力してください')])
    title = StringField('題名')
    text = TextAreaField('メッセージ本文(必須)',validators=[DataRequired()])
    submit = SubmitField('送信')