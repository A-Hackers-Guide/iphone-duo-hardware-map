# `GrimaldiAPDSEventSource`

- Image: [`/System/Library/PrivateFrameworks/CoreBrightness.framework/CoreBrightness`](../userland/System__Library__PrivateFrameworks__CoreBrightness.framework__CoreBrightness.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `CBGrimaldiEventSource`
- 3 instance variables, 4 properties, 6 instance methods, 0 class methods

## Instance variables

```
^v _apdsHandle;
@"NSObject<OS_os_log>" _logHandle;
^v APDSGlobalCorrectionSymbolAddr;
```

## Properties

```
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[GrimaldiAPDSEventSource init];
-[GrimaldiAPDSEventSource dealloc];
-[GrimaldiAPDSEventSource description];
-[GrimaldiAPDSEventSource getCoexFlags:];
-[GrimaldiAPDSEventSource getGlobalCorrectionFactor:];
-[GrimaldiAPDSEventSource requestEventOn:withNsamples:withCallback:];
```
