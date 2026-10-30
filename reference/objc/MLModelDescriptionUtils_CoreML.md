# `MLModelDescriptionUtils`

- Image: [`/System/Library/Frameworks/CoreML.framework/CoreML`](../userland/System__Library__Frameworks__CoreML.framework__CoreML.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 0 instance variables, 0 properties, 0 instance methods, 11 class methods

## Class methods

```
+[MLModelDescriptionUtils createMetaData:];
+[MLModelDescriptionUtils copyFeatureDescriptionFrom:to:error:];
+[MLModelDescriptionUtils createFeatureTypeFromFeatureDescription:error:];
+[MLModelDescriptionUtils createModelDescription:error:];
+[MLModelDescriptionUtils getArrayFeatureTypeFromConstraint:];
+[MLModelDescriptionUtils getDictionaryFeatureTypeFromConstraint:error:];
+[MLModelDescriptionUtils getImageFeatureTypeFromConstraint:];
+[MLModelDescriptionUtils getSequenceFeatureTypeFromConstraint:error:];
+[MLModelDescriptionUtils getStateFeatureTypeFromConstraint:];
+[MLModelDescriptionUtils saveModelDescription:toSpecification:error:];
+[MLModelDescriptionUtils validateAllFeatureDescriptions:hasAnyFeatureTypeIn:minimalCount:maximumCount:debugLabel:error:];
```
