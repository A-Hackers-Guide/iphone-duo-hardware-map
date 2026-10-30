# `ABDProcessor`

- Image: [`/System/Library/PrivateFrameworks/ISPKit.framework/ISPKit`](../userland/System__Library__PrivateFrameworks__ISPKit.framework__ISPKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 5 instance variables, 1 properties, 7 instance methods, 0 class methods

## Instance variables

```
@"NSMutableDictionary" _networks;
@"NSString" _networksDefaultPath;
@"NSString" _networksCurrentPath;
@"NSUserDefaults" _userDefaults;
@"ABDStatistics" _lastProcessingStats;
```

## Properties

```
@property (T@"ABDStatistics",R,&,N,V_lastProcessingStats) lastProcessingStats;
```

## Instance methods

```
-[ABDProcessor init];
-[ABDProcessor process:into:configId:metadata:];
-[ABDProcessor lastProcessingStats];
-[ABDProcessor nameOfConfig:];
-[ABDProcessor networkById:forWidth:andHeight:];
-[ABDProcessor networkById:forBuffer:];
-[ABDProcessor process:into:coordinateMap:configId:];
```
