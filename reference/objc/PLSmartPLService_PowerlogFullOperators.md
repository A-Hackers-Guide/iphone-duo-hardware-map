# `PLSmartPLService`

- Image: [`/System/Library/PrivateFrameworks/PowerlogFullOperators.framework/PowerlogFullOperators`](../userland/System__Library__PrivateFrameworks__PowerlogFullOperators.framework__PowerlogFullOperators.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `PLService`
- 1 instance variables, 1 properties, 14 instance methods, 5 class methods

## Instance variables

```
@"NSMutableDictionary" _smartPLHelpers;
```

## Properties

```
@property (T@"NSMutableDictionary",&,V_smartPLHelpers) smartPLHelpers;
```

## Class methods

```
+[PLSmartPLService entryEventPointDefinitions];
+[PLSmartPLService load];
+[PLSmartPLService defaults];
+[PLSmartPLService entryEventPointDefinitionSample];
+[PLSmartPLService entryEventPointDefinitionSmartTrigger];
```

## Instance methods

```
-[PLSmartPLService init];
-[PLSmartPLService initOperatorDependancies];
-[PLSmartPLService logEventPointHeap];
-[PLSmartPLService logEventPointHeapForProcessName:];
-[PLSmartPLService logEventPointSample];
-[PLSmartPLService logEventPointSampleForProcessName:];
-[PLSmartPLService logEventPointSmartPLFiredFromAuxilary:withReason:];
-[PLSmartPLService logEventPointStackShot];
-[PLSmartPLService logEventPointStackShotWithReason:];
-[PLSmartPLService logEventPointVMMap];
-[PLSmartPLService logEventPointVMMapForProcessName:];
-[PLSmartPLService setSmartPLHelpers:];
-[PLSmartPLService smartPLHelpers];
-[PLSmartPLService vmmapProcessName:];
```
