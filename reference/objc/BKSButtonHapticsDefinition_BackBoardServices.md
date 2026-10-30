# `BKSButtonHapticsDefinition`

- Image: [`/System/Library/PrivateFrameworks/BackBoardServices.framework/BackBoardServices`](../userland/System__Library__PrivateFrameworks__BackBoardServices.framework__BackBoardServices.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSSecureCoding`
- 2 instance variables, 10 properties, 24 instance methods, 2 class methods

## Instance variables

```
@"BSMutableSettings" _settings;
B _representsHomeButton;
```

## Properties

```
@property (TB,N,V_representsHomeButton) representsHomeButton;
@property (T@"BSSettings",R,N,G_BSSettings,V_settings) BSSettings;
@property (Tq,R,N,GisLongPressEnabled) longPressEnabled;
@property (Td,N) minimumMultiplePressTimeInterval;
@property (Td,N) maximumMultiplePressTimeInterval;
@property (Td,N) minimumLongPressTimeInterval;
@property (Td,N) maximumLongPressTimeInterval;
@property (Tq,N) maximumPressCount;
@property (Tq,N) maximumTapCount;
@property (Tq,N) clickHapticAssetType;
```

## Class methods

```
+[BKSButtonHapticsDefinition supportsSecureCoding];
+[BKSButtonHapticsDefinition definitionForHomeButton];
```

## Instance methods

```
-[BKSButtonHapticsDefinition setMaximumLongPressTimeInterval:];
-[BKSButtonHapticsDefinition _initWithBSSettings:];
-[BKSButtonHapticsDefinition init];
-[BKSButtonHapticsDefinition setRepresentsHomeButton:];
-[BKSButtonHapticsDefinition isLongPressEnabled];
-[BKSButtonHapticsDefinition _BSSettings];
-[BKSButtonHapticsDefinition maximumPressCount];
-[BKSButtonHapticsDefinition setMinimumMultiplePressTimeInterval:];
-[BKSButtonHapticsDefinition setMaximumPressCount:];
-[BKSButtonHapticsDefinition setMinimumLongPressTimeInterval:];
-[BKSButtonHapticsDefinition representsHomeButton];
-[BKSButtonHapticsDefinition maximumMultiplePressTimeInterval];
-[BKSButtonHapticsDefinition encodeWithCoder:];
-[BKSButtonHapticsDefinition minimumLongPressTimeInterval];
-[BKSButtonHapticsDefinition clickHapticAssetType];
-[BKSButtonHapticsDefinition description];
-[BKSButtonHapticsDefinition initWithCoder:];
-[BKSButtonHapticsDefinition setMaximumMultiplePressTimeInterval:];
-[BKSButtonHapticsDefinition updateFromDefinition:withChangeInspectorBlock:];
-[BKSButtonHapticsDefinition setClickHapticAssetType:];
-[BKSButtonHapticsDefinition maximumLongPressTimeInterval];
-[BKSButtonHapticsDefinition maximumTapCount];
-[BKSButtonHapticsDefinition setMaximumTapCount:];
-[BKSButtonHapticsDefinition minimumMultiplePressTimeInterval];
```
