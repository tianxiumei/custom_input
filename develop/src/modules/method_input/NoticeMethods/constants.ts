import { ENotifyMode } from 'apis/alert/notice'
import deployService, { DeployEnv } from 'services/base/deploy'

export interface IMethodItem {
  active: boolean
  template: string
}

export const defaultMethodItem = {
  active: false,
  template: ''
}

export interface IMethod {
  [ENotifyMode.EMAIL]: IMethodItem
  [ENotifyMode.WECHAT]: IMethodItem
  [ENotifyMode.DINGDING]: IMethodItem
  citicPhone?: IMethodItem
}

export const defaultMethod: IMethod = {
  [ENotifyMode.EMAIL]: defaultMethodItem,
  [ENotifyMode.WECHAT]: defaultMethodItem,
  [ENotifyMode.DINGDING]: defaultMethodItem,
  citicPhone:
    deployService.deployEnv === DeployEnv.Citic ? defaultMethodItem : undefined
}
