import React from 'react'
import ReactDom from 'react-dom'
import { Bind } from 'lodash-decorators'
import BaseInput from '../../component/baseInput'
import NoticeMethods from './NoticeMethods'

import '../../global/styles/style.less'

export default class MethodInput extends BaseInput {
  @Bind
  async render(props: any) {
    if (this.element) {
      ReactDom.render(
        <NoticeMethods
          readonly={props.readonly}
          onChange={props.onChange}
          getPopupContainer={props.getPopupContainer}
          value={props.value}
        />,
        this.element
      )
    }
  }
}
