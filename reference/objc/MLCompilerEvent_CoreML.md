# `MLCompilerEvent`

- Image: [`/System/Library/Frameworks/CoreML.framework/CoreML`](../userland/System__Library__Frameworks__CoreML.framework__CoreML.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `CUTCoreAnalyticsMetric`
- 9 instance variables, 15 properties, 21 instance methods, 0 class methods

## Instance variables

```
@"NSString" _modelName;
@"NSString" _modelHash;
@"NSNumber" _modelType;
@"NSNumber" _modelOrigin;
@"NSString" _modelVersion;
@"NSString" _modelCompiledWithVersion;
@"NSString" _compilerVersion;
@"NSNumber" _milUpgradeStatus;
@"NSString" _milUpgradeFailureReason;
```

## Properties

```
@property (T@"NSString",C,N,V_modelName) modelName;
@property (T@"NSString",C,N,V_modelHash) modelHash;
@property (T@"NSNumber",C,N,V_modelType) modelType;
@property (T@"NSNumber",C,N,V_modelOrigin) modelOrigin;
@property (T@"NSString",C,N,V_modelVersion) modelVersion;
@property (T@"NSString",C,N,V_modelCompiledWithVersion) modelCompiledWithVersion;
@property (T@"NSString",C,N,V_compilerVersion) compilerVersion;
@property (T@"NSNumber",C,N,V_milUpgradeStatus) milUpgradeStatus;
@property (T@"NSString",C,N,V_milUpgradeFailureReason) milUpgradeFailureReason;
@property (T@"NSDictionary",R) dictionaryRepresentation;
@property (T@"NSString",R) name;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[MLCompilerEvent modelVersion];
-[MLCompilerEvent modelHash];
-[MLCompilerEvent modelOrigin];
-[MLCompilerEvent init];
-[MLCompilerEvent compilerVersion];
-[MLCompilerEvent setCompilerVersion:];
-[MLCompilerEvent setModelVersion:];
-[MLCompilerEvent setModelOrigin:];
-[MLCompilerEvent setModelHash:];
-[MLCompilerEvent setModelName:];
-[MLCompilerEvent modelType];
-[MLCompilerEvent name];
-[MLCompilerEvent modelName];
-[MLCompilerEvent dictionaryRepresentation];
-[MLCompilerEvent setModelType:];
-[MLCompilerEvent milUpgradeFailureReason];
-[MLCompilerEvent milUpgradeStatus];
-[MLCompilerEvent modelCompiledWithVersion];
-[MLCompilerEvent setMilUpgradeFailureReason:];
-[MLCompilerEvent setMilUpgradeStatus:];
-[MLCompilerEvent setModelCompiledWithVersion:];
```
