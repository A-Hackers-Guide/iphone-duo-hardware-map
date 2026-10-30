# `WAChanInfo`

- Image: [`/System/Library/PrivateFrameworks/WiFiAnalytics.framework/WiFiAnalytics`](../userland/System__Library__PrivateFrameworks__WiFiAnalytics.framework__WiFiAnalytics.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 3 instance variables, 3 properties, 8 instance methods, 3 class methods

## Instance variables

```
s _channel;
s _band;
i _simplifiedChannelFlags;
```

## Properties

```
@property (Ts,V_channel) channel;
@property (Ts,V_band) band;
@property (Ti,V_simplifiedChannelFlags) simplifiedChannelFlags;
```

## Class methods

```
+[WAChanInfo chanInfoWithChannel:band:];
+[WAChanInfo chanInfoWithObjectHavingChInfo:withPrefix:];
+[WAChanInfo simplifiedChannelFlags:];
```

## Instance methods

```
-[WAChanInfo setChannel:];
-[WAChanInfo channel];
-[WAChanInfo band];
-[WAChanInfo setBand:];
-[WAChanInfo description];
-[WAChanInfo chanInfoDictionary];
-[WAChanInfo setSimplifiedChannelFlags:];
-[WAChanInfo simplifiedChannelFlags];
```
