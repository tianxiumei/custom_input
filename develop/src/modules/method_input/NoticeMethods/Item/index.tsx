import * as React from 'react'
import classnames from 'classnames'
import { observer } from 'mobx-react'
import { computed } from 'mobx'
import { get } from 'lodash'
import { TagList, Selector } from '@qn-pandora/pandora-component'
import { TemplateLocale } from 'constants/language/alert/notice/template/type'
import { formatString } from 'services/base/language'
import bind from 'utils/bind'
import { ENotifyMode } from 'apis/alert/notice/model'
import { AlertLocale } from 'constants/language/alert/type'
import { IMethodItem, defaultMethodItem } from '../constants'

import * as style from './style.mless'

const { TagSwitch } = TagList

export interface IItemProps {
  title?: string
  icon: React.ReactElement
  source: any
  value?: IMethodItem
  readonly?: boolean
  isLast?: boolean
  onView?: (name: string, notifyNode: ENotifyMode) => void
  onChange?: (value: IMethodItem, source: any) => void
  getPopupContainer?: () => HTMLElement
  templateOptions?: IKeyValues<string>
  hideTempSelector?: boolean
}

@observer
export default class Item extends React.Component<IItemProps, any> {
  @bind
  handleActiveChange(active: boolean) {
    const { source, value, onChange } = this.props
    const { template } = value || defaultMethodItem
    if (onChange) {
      onChange({ active, template }, source)
    }
  }

  @bind
  handleTemplateChange(template: string) {
    const { source, value, onChange } = this.props
    const { active } = value || defaultMethodItem
    if (onChange) {
      onChange({ active, template }, source)
    }
  }

  @computed
  get selectorOptions() {
    const { templateOptions = {} } = this.props
    return {
      ...templateOptions,
      '': formatString(TemplateLocale.default_template)
    }
  }

  @bind
  handleView() {
    const { onView, value, templateOptions, source } = this.props
    const id = get(value, 'template') || ''
    if (onView) {
      onView(templateOptions![id], source)
    }
  }

  render() {
    const {
      title,
      icon,
      value,
      getPopupContainer,
      hideTempSelector,
      onView,
      readonly,
      templateOptions
    } = this.props
    const { active, template } = value || defaultMethodItem
    const renderIcon = React.cloneElement(icon, {
      className: classnames(icon.props.className, style.icon, {
        [style.active]: active && !readonly,
        [style.readonly]: readonly
      })
    })

    if (!active && readonly) {
      return ''
    }

    return (
      <div
        className={classnames(style.root, { [style.last]: this.props.isLast })}
      >
        {!readonly && (
          <TagSwitch
            type="primary"
            className={style.tag}
            title={title}
            getPopupContainer={getPopupContainer}
            active={active}
            onChange={this.handleActiveChange}
          >
            {renderIcon}
          </TagSwitch>
        )}
        {readonly && renderIcon}
        {!hideTempSelector && !readonly && (
          <Selector
            className={classnames(style.selector, {
              [style.disabled]: !active
            })}
            value={template}
            onChange={this.handleTemplateChange as any}
            options={this.selectorOptions}
            getPopupContainer={getPopupContainer}
          />
        )}
        {readonly && (
          <span>
            {get(templateOptions, template) ||
              formatString(AlertLocale.notice.template.default_template)}
          </span>
        )}
        {onView && active && (
          <span className={style.view} onClick={this.handleView}>
            {formatString(AlertLocale.notice.view)}
          </span>
        )}
      </div>
    )
  }
}
