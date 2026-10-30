# `DYMTLDerivedCounterSupport`

- Image: [`/System/Library/PrivateFrameworks/MTLToolsDeviceSupport.framework/MTLToolsDeviceSupport`](../userland/System__Library__PrivateFrameworks__MTLToolsDeviceSupport.framework__MTLToolsDeviceSupport.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 5 instance variables, 5 properties, 11 instance methods, 1 class methods

## Instance variables

```
@"NSMutableDictionary" _counterDictionary;
@"NSString" _derivedCounterScript;
@"NSString" _analysisScript;
@"NSMutableDictionary" _configurationVariables;
@"NSString" _metalPluginName;
```

## Properties

```
@property (T@"NSMutableDictionary",R,N,V_counterDictionary) counterDictionary;
@property (T@"NSString",R,N,V_derivedCounterScript) derivedCounterScript;
@property (T@"NSString",R,N,V_analysisScript) analysisScript;
@property (T@"NSMutableDictionary",R,N,V_configurationVariables) configurationVariables;
@property (T@"NSString",R,N,V_metalPluginName) metalPluginName;
```

## Class methods

```
+[DYMTLDerivedCounterSupport mergeDictionaries:right:];
```

## Instance methods

```
-[DYMTLDerivedCounterSupport initWithAcceleratorPort:];
-[DYMTLDerivedCounterSupport init];
-[DYMTLDerivedCounterSupport initWithMTLDevice:];
-[DYMTLDerivedCounterSupport metalPluginName];
-[DYMTLDerivedCounterSupport analysisScript];
-[DYMTLDerivedCounterSupport configurationVariables];
-[DYMTLDerivedCounterSupport counterDictionary];
-[DYMTLDerivedCounterSupport derivedCounterScript];
-[DYMTLDerivedCounterSupport _addGPUTimeEntry];
-[DYMTLDerivedCounterSupport _loadAnalysis:vendorStringNames:vendorScriptPrefix:];
-[DYMTLDerivedCounterSupport addAnalysisWithPrefix:andScriptPrefix:];
```
