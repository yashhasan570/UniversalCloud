/*
 * @Author: LinkLeong link@icewhale.com
 * @Date: 2021-09-30 18:18:14
 * @LastEditors: LinkLeong
 * @LastEditTime: 2022-08-31 17:04:02
 * @FilePath: /UniversalCloud/pkg/config/config.go
 * @Description:
 * @Website: https://www.universalcloud.app
 * Copyright (c) 2022 by icewhale, All Rights Reserved.
 */
package config

import (
	"path/filepath"

	"github.com/yashhasan570/UniversalCloud-Common/utils/constants"
)

var UniversalCloudConfigFilePath = filepath.Join(constants.DefaultConfigPath, "universalcloud.conf")
