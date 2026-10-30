# `FigCoreTelephony`

- Image: [`/System/Library/Frameworks/MediaToolbox.framework/MediaToolbox`](../userland/System__Library__Frameworks__MediaToolbox.framework__MediaToolbox.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `CoreTelephonyClientRegistrationDelegate`, `CoreTelephonyClientDataDelegate`
- 6 instance variables, 4 properties, 12 instance methods, 0 class methods

## Instance variables

```
@"CoreTelephonyClient" ctClient;
^{OpaqueFigReentrantMutex=} _cellStatsLock;
@"NSDictionary" cellStats;
@"NSString" carrierName;
C lssAnomaly;
C oosAnomaly;
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
-[FigCoreTelephony signalStrengthChanged:info:];
-[FigCoreTelephony preferredDataSimChanged:];
-[FigCoreTelephony withCellStatsLock:];
-[FigCoreTelephony dealloc];
-[FigCoreTelephony initWithError:];
-[FigCoreTelephony copyRegistrationStatusValueForContext:];
-[FigCoreTelephony updateCellStatsWithLatestSignalStrengthInfo:];
-[FigCoreTelephony isOOSAnomaly];
-[FigCoreTelephony isLSSAnomaly];
-[FigCoreTelephony saveCarrierName];
-[FigCoreTelephony getLatestCellStats];
-[FigCoreTelephony displayStatusChanged:status:];
```
