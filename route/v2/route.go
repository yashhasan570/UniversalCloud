package v2

import (
	"github.com/yashhasan570/UniversalCloud/codegen"
	"github.com/yashhasan570/UniversalCloud/service"
)

type UniversalCloud struct {
	fileUploadService *service.FileUploadService
}

func NewUniversalCloud() codegen.ServerInterface {
	return &UniversalCloud{
		fileUploadService: service.NewFileUploadService(),
	}
}
