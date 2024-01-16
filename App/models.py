# 数据模型
from .extensions import db
from datetime import datetime





class AccountModel(db.Model):
    __tablename__ = 'account'
    # 用户唯一ID：主键
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    # 用户名
    name = db.Column(db.String(200), nullable=False)
    # 密码
    password = db.Column(db.String(200), nullable=False)
    # 电话
    phone = db.Column(db.String(200), nullable=False)
    # 电子邮件
    email = db.Column(db.String(200),nullable=False)
    # 注册时间
    join_time = db.Column(db.DateTime, default = datetime.now)
    # 身份（用户/管理员）
    authority = db.Column(db.String(200), nullable=False)



    def to_json(self):
        dict = self.__dict__
        if '_sa_instance_state' in dict:
            del dict['_sa_instance_state']
        return dict

class UserQCModel(db.Model):
    __tablename__ = 'qc'
    # 认证编码
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    # 审核状态
    audit_status = db.Column(db.String(200), nullable=False)


    # 工商信息
    # 统一社会信用代码
    c_unified_social_credit_code = db.Column(db.String(200),nullable=False)
    # 企业名称
    c_name = db.Column(db.String(200),nullable=False)
    # 企业类型
    c_type = db.Column(db.String(200),nullable=False)
    # 经营范围
    c_scrope = db.Column(db.Text,nullable=False)
    # 营业执照类型
    c_license_type = db.Column(db.String(200),nullable=False)
    # 营业执照
    c_license = db.Column(db.String(200), nullable=False)

    # 经营者信息
    # 经营者姓名
    m_name =  db.Column(db.String(200), nullable=False)
    # 手机号码
    m_phone = db.Column(db.String(200), nullable=False)
    # 经营者证件类型
    m_license_type = db.Column(db.String(200), nullable=False)
    # 经营者证件
    m_license = db.Column(db.String(200), nullable=False)


    # 开户银行信息
    # 开户账户
    b_account = db.Column(db.String(200), nullable=False)
    # 开户银行
    b_bank = db.Column(db.String(200), nullable=False)
    # 开户名称
    b_account_name = db.Column(db.String(200), nullable=False)
    # 开户机构
    b_institution = db.Column(db.String(200), nullable=False)
    # 开户信息
    b_account_info = db.Column(db.String(200), nullable=False)

    # 联系人信息
    # 联系人姓名
    l_name = db.Column(db.String(200), nullable=False)
    # 地理区域
    l_area = db.Column(db.String(200))
    # 通讯地址
    l_address = db.Column(db.Text, nullable=False)
    # 邮政编码
    l_code = db.Column(db.Integer, nullable=False)
    # 电子邮箱
    l_email = db.Column(db.String(200), nullable=False)
    # 企业网址
    l_website = db.Column(db.String(200), nullable=False)
    # 手机号码
    l_phone = db.Column(db.String(200), nullable=False)

    # account => AccountModel
    account_id = db.Column(db.Integer, db.ForeignKey('account.id'), nullable=False)
    account = db.relationship('AccountModel', backref='qc')



    def to_json(self):
        dict = self.__dict__
        if '_sa_instance_state' in dict:
            del dict['_sa_instance_state']
        return dict

class DataAssetModel(db.Model):
    __tablename__ = 'data_asset'
    # 数据资产唯一ID：主键
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    # 数据资产名称
    name = db.Column(db.String(200), nullable=False)
    # 数据资产关键词
    keyword = db.Column(db.String(200), nullable=False)
    # 数据资产产业类别
    industry_division = db.Column(db.String(200), nullable=False)
    # 数据资产类别
    type = db.Column(db.String(200), nullable=False)
    # 数据资产权属范围
    property_range = db.Column(db.String(200), nullable=False)
    # 数据资产规模
    size = db.Column(db.String(200), nullable=False)
    # 数据资产源文件（文件地址？）
    data = db.Column(db.String(200), nullable=False)
    # 数据资产溯源文件 （文件地址？）
    traceability_certification_documents = db.Column(db.String(200), nullable=False)
    # 数据质量报告 （文件地址？）
    quality_assessment_report = db.Column(db.String(200), nullable=False)
    # 审核状态
    audit_status = db.Column(db.String(200), nullable=False)
    # 文件格式：csv sql
    format = db.Column(db.String(200),nullable=False)
    # 收集时间
    begin_time = db.Column(db.DateTime,nullable=False)
    # 更新时间
    renew_time = db.Column(db.DateTime,nullable=False)

    # User表外键
    # owner => AccountModel
    owner_id = db.Column(db.Integer, db.ForeignKey('account.id'))
    owner = db.relationship('AccountModel', backref='data_asset')



    def to_json(self):
        dict = self.__dict__
        if '_sa_instance_state' in dict:
            del dict['_sa_instance_state']
        return dict

class DataProductsModel(db.Model):
    __tablename__ = 'data_products'
    # 数据资产唯一ID：主键
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)


    # 商品名称
    name = db.Column(db.String(200), nullable=False)
    # 审核状态
    audit_status = db.Column(db.String(200), nullable=False)
    # 商品上架状态
    market_status = db.Column(db.String(200),nullable=False )
    # 商品标定价格
    nominal_price = db.Column(db.Integer)
    # 商品预览图
    pre_img= db.Column(db.String(200))
    # 商品描述
    products_description = db.Column(db.Text)
    # 商品引用场景
    application_scenario = db.Column(db.Text)

    # 商品交易权属范畴
    property_range = db.Column(db.String(200))
    # 权属到期时间
    time_limit = db.Column(db.DateTime, nullable=False)


    # data_asset => DataAssetModel
    data_asset_id = db.Column(db.Integer, db.ForeignKey('data_asset.id'))
    data_asset = db.relationship('DataAssetModel', backref='data_products')
    # owner => AccountModel
    owner_id = db.Column(db.Integer, db.ForeignKey('account.id'))
    account = db.relationship('AccountModel', backref='data_products')


    def to_json(self):
        dict = self.__dict__
        if '_sa_instance_state' in dict:
            del dict['_sa_instance_state']
        return dict

class TransactionContractModel(db.Model):
    __tablename__ = 'transaciton_contract'
    # 交易合同唯一ID:主键
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    # 交易时间
    tradding_time = db.Column(db.DateTime, nullable=False)
    # 交易是否生效
    effective_or_not = db.Column(db.String(200), nullable=False)

    #建立关系
    #   第一个参数：关联的模型（表）
    #   第二个参数：反向引用的名称 比如 buyer ,让Account表反过来得到交易合同的信息：Account.

    # data_products => DataproductsModel
    # TransactionContract.data_products() 合同中的数据商品
    data_products_id = db.Column(db.Integer, db.ForeignKey('data_products.id'))
    data_products = db.relationship('DataProductsModel', backref='transaciton_contracts')

    # buyer => AccountModel
    # TransactionContractModel.buyer() 交易合同的买方
    buyer_id = db.Column(db.Integer, db.ForeignKey('account.id'))
    buyer = db.relationship('AccountModel', backref='tc_buyer', foreign_keys=[buyer_id])

    # seller => AccountModel
    # TransactionContractModel.buyer() 交易合同的买方
    seller_id = db.Column(db.Integer, db.ForeignKey('account.id'))
    seller = db.relationship('AccountModel', backref='tc_seller', foreign_keys=[seller_id])


    def to_json(self):
        dict = self.__dict__
        if '_sa_instance_state' in dict:
            del dict['_sa_instance_state']
        return dict


