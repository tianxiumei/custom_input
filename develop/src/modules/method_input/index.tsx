import React from 'react'
import ReactDom from 'react-dom'
import { Spin } from 'antd'
import { action, observable } from 'mobx'
import { get } from 'lodash'
import { Bind } from 'lodash-decorators'
import { appEnv, utils } from '@qn-pandora/app-sdk'
import { Selector } from '@qn-pandora/pandora-component'
import BaseInput from '../base-input'

import style from './style.module.less'
import NoticeMethods from './NoticeMethods'


const { fetch } = utils

interface IOption {
    text: string
    value: string
}

export default class MthodInput extends BaseInput {
    @observable.ref options: IOption[] = []
    @observable tenanatid: string = ''
    @observable isLoading: boolean = false

    @Bind
    @action
    setOptions(options: IOption[]) {
        this.options = options
    }

    @Bind
    @action
    setTenanatid(tenanatid: string) {
        this.tenanatid = tenanatid
    }

    @Bind
    @action
    setIsLoading(isLoading: boolean) {
        this.isLoading = isLoading
    }

    @Bind
    async listApiOptions() {
        if (this.tenanatid) {
            try {
                this.setIsLoading(true)
                const data: any = await fetch(
                    `${appEnv.basepath}/custom/v1/src_trigger/tenants/users?tenantid=${this.tenanatid} `
                )
                const options = get(data, 'data') || []
                this.setOptions(
                    options.map((item: any) => ({
                        text: item.name,
                        value: item.id
                    }))
                )
                this.setIsLoading(false)
            } catch (error) {
                console.error(error)
                this.setIsLoading(false)
            }
        }
    }

    @Bind
    async render(props: any) {
        if (this.element) {
            ReactDom.render(
                <div className={style.spinContainter}>
                    <Spin className={style.spin} spinning={true} />
                </div>,
                this.element
            )
        }
        const tenanatid = get(props.values, 'tenanatid')
        if (tenanatid !== this.tenanatid) {
            this.setTenanatid(tenanatid)
            await this.listApiOptions()
        }
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
