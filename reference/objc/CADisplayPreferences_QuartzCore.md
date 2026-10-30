# `CADisplayPreferences`

- Image: [`/System/Library/Frameworks/QuartzCore.framework/QuartzCore`](../userland/System__Library__Frameworks__QuartzCore.framework__QuartzCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`, `NSMutableCopying`
- 1 instance variables, 5 properties, 15 instance methods, 0 class methods

## Instance variables

```
^{CADisplayPreferencesPriv=BiBB} _priv;
```

## Properties

```
@property (TB,N) matchContent;
@property (T@"NSString",C,N) preferredHdrMode;
@property (Ti,R,N) _preferredHdrType;
@property (TB,N) prefersHighRefreshRate;
@property (TB,R,N) prefersVariableRefreshRate;
```

## Instance methods

```
-[CADisplayPreferences mutableCopyWithZone:];
-[CADisplayPreferences init];
-[CADisplayPreferences dealloc];
-[CADisplayPreferences initWithPreferences:];
-[CADisplayPreferences copyWithZone:];
-[CADisplayPreferences _preferredHdrType];
-[CADisplayPreferences initWithMatchContent:preferredHdrType:prefersHighRefreshRate:prefersVRR:];
-[CADisplayPreferences matchContent];
-[CADisplayPreferences preferredHdrMode];
-[CADisplayPreferences prefersHighRefreshRate];
-[CADisplayPreferences prefersVariableRefreshRate];
-[CADisplayPreferences setMatchContent:];
-[CADisplayPreferences setPreferredHdrMode:];
-[CADisplayPreferences setPrefersHighRefreshRate:];
-[CADisplayPreferences setPrefersVariableRefreshRate:];
```
