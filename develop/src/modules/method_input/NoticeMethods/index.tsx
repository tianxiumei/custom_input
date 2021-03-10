import React from 'react'
import { computed } from 'mobx'
import { observer } from 'mobx-react'
import { get } from 'lodash'
import { TagList } from '@qn-pandora/pandora-component'
import { Icon } from '@qn-pandora/pandora-component-icons'
import bind from 'utils/bind'
import errorBoundary from 'hoc/errorBoundary'
import { FontIcon } from 'components/Common'
import { formatString } from 'services/base/language'
import { AlertLocale } from 'constants/language/alert/type'
import deployService from 'services/base/deploy'
import { IMethod, IMethodItem, defaultMethod } from './constants'
import Store from './store'
import Item from './Item'
import { ENotifyMode } from '../constants'

interface IMethondProps {
  value?: IMethod
  readonly?: boolean
  onView?: (name: string, notifyNode: ENotifyMode) => void
  onChange?: (value: IMethod) => void
  getPopupContainer?: () => HTMLElement
}

@observer
export class NoticeMethods extends React.Component<IMethondProps, any> {
  store = new Store()

  @computed
  get templateOptions() {


    return res
  }

  @bind
  handleMethodsChange(item: IMethodItem, source: string) {
    const { value = defaultMethod, onChange } = this.props
    if (onChange) {
      onChange({
        ...value,
        [source]: item
      })
    }
  }

  render() {
    const {
      value = defaultMethod,
      getPopupContainer,
      onView,
      readonly
    } = this.props
    return (
      <TagList>
        <Item
          onView={onView}
          readonly={readonly}
          title={formatString(AlertLocale.email)}
          icon={<Icon type="mail" />}
          getPopupContainer={getPopupContainer}
          source={ENotifyMode.EMAIL}
          value={value[ENotifyMode.EMAIL]}
          onChange={this.handleMethodsChange}
        />
        <Item
          onView={onView}
          readonly={readonly}
          title={formatString(AlertLocale.wechat)}
          icon={<FontIcon type="work-weixin" />}
          getPopupContainer={getPopupContainer}
          source={ENotifyMode.WECHAT}
          value={value[ENotifyMode.WECHAT]}
          onChange={this.handleMethodsChange}
          templateOptions={this.templateOptions[ENotifyMode.WECHAT]}
        />
      </TagList>
    )
  }
}

export default errorBoundary(NoticeMethods)
