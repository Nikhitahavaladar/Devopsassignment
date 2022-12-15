package parse

import (
	"strings"

	"github.com/hashicorp/hcl/v2"
	"github.com/turbot/steampipe/pkg/steampipeconfig/modconfig"
)

func GetMetadataForParsedResource(resourceName string, srcRange hcl.Range, fileData map[string][]byte, mod *modconfig.Mod) (*modconfig.ResourceMetadata, error) {
	// convert the name into a short name
	parsedName, err := modconfig.ParseResourceName(resourceName)
	if err != nil {
		return nil, err
	}
	m := &modconfig.ResourceMetadata{
		ResourceName:     parsedName.Name,
		FileName:         srcRange.Filename,
		StartLineNumber:  srcRange.Start.Line,
		EndLineNumber:    srcRange.End.Line,
		IsAutoGenerated:  false,
		SourceDefinition: getSourceDefinition(srcRange, fileData),
	}
	// update the 'ModName' and 'ModShortName' fields
	m.SetMod(mod)
	return m, nil
}

func getSourceDefinition(sourceRange hcl.Range, fileData map[string][]byte) string {
	filename := sourceRange.Filename
	fileBytes, ok := fileData[filename]
	if !ok {
		return ""
	}

	source := strings.Join(
		strings.Split(string(fileBytes), "\n")[sourceRange.Start.Line-1:sourceRange.End.Line], "\n")
	return source
}
