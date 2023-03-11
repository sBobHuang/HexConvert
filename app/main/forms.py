#!/usr/bin/python
# -*- coding: utf-8 -*-
from flask_wtf import FlaskForm
from flask_wtf.file import FileRequired
from wtforms import StringField, SubmitField, BooleanField, IntegerField, SelectField, FileField
from wtforms.validators import DataRequired, Length, Email, ValidationError


class UploadForm(FlaskForm):
    name = StringField('姓名', validators=[DataRequired()])
    studentID = StringField('学号', validators=[DataRequired()])
    course = SelectField(
        label='科目',
        choices=[('计算机导论', '计算机导论')
                 ],
        coerce=str
    )
    homeWork = SelectField(
        label='作业名称',
        choices=[('作业1', '作业1'),
                 ('作业2', '作业2')
                 ],
        coerce=str
    )
    file = FileField('上传文件', validators=[FileRequired()])
    submit = SubmitField('提交')


class CalculatorForm(FlaskForm):
    form_title = '计算器'
    calculator_str = StringField('算式', validators=[DataRequired()])
    is_ans_hex_format = BooleanField('结果十六进制')
    submit9 = SubmitField('提交')


class DownloadForm(FlaskForm):
    url = StringField('url', validators=[DataRequired(), Length(1, 200)])
    download_id = None
    submit = SubmitField('提交')


class HexStr2BinStrForm(FlaskForm):
    form_title = '十六进制转二进制'
    hex_str = StringField('十六进制串', validators=[DataRequired(), Length(1, 200)])
    download_id = None
    submit1 = SubmitField('提交')


class Dec2BinStrForm(FlaskForm):
    form_title = '十进制转二进制'
    dec = IntegerField('十进制数字')
    bits_of_digit = IntegerField('位数', default=8)
    submit2 = SubmitField('提交')


class BinStr2DecForm(FlaskForm):
    form_title = '二进制转十进制'
    bin_str = StringField('二进制串', validators=[DataRequired(), Length(1, 200)])
    submit3 = SubmitField('提交')


class HexStr2DecForm(FlaskForm):
    form_title = '十六进制转十进制'
    hex_str = StringField('十六进制串', validators=[DataRequired(), Length(1, 200)])
    submit4 = SubmitField('提交')


class ComplementBinStr2DecForm(FlaskForm):
    form_title = '补码计算'
    bin_str = StringField('二进制补码串', validators=[DataRequired(), Length(1, 200)])
    submit5 = SubmitField('提交')


class Dec2ComplementBinStrForm(FlaskForm):
    form_title = '十进制求补码'
    dec = IntegerField('十进制数字')
    bits_of_digit = IntegerField('位数', default=16)
    submit6 = SubmitField('提交')


class StrLengthForm(FlaskForm):
    form_title = '数字长度'
    num_str = StringField('字符串', validators=[DataRequired(), Length(1, 200)])
    submit7 = SubmitField('提交')


class BinStr2HexStrForm(FlaskForm):
    form_title = '二进制转十六进制'
    bin_str = StringField('二进制串', validators=[DataRequired(), Length(1, 200)])
    submit8 = SubmitField('提交')


class Dec2HexStrForm(FlaskForm):
    form_title = '十进制转十六进制'
    dec = IntegerField('十进制数字')
    bits_of_digit = IntegerField('位数', default=0)
    submit10 = SubmitField('提交')
