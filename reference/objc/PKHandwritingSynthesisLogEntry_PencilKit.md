# `PKHandwritingSynthesisLogEntry`

- Image: [`/System/Library/Frameworks/PencilKit.framework/PencilKit`](../userland/System__Library__Frameworks__PencilKit.framework__PencilKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 6 instance variables, 7 properties, 9 instance methods, 0 class methods

## Instance variables

```
@"NSLocale" _locale;
d _duration;
@"NSArray" _synthesizedStrokes;
@"NSArray" _originalStrokes;
@"NSArray" _contextStrokes;
@"NSMutableDictionary" _debugInfo;
```

## Properties

```
@property (T@"NSMutableDictionary",R,V_debugInfo) debugInfo;
@property (T@"NSLocale",R,V_locale) locale;
@property (Td,R,V_duration) duration;
@property (T@"NSDictionary",R) description;
@property (T@"NSArray",R,V_synthesizedStrokes) synthesizedStrokes;
@property (T@"NSArray",R,V_originalStrokes) originalStrokes;
@property (T@"NSArray",R,V_contextStrokes) contextStrokes;
```

## Instance methods

```
-[PKHandwritingSynthesisLogEntry debugInfo];
-[PKHandwritingSynthesisLogEntry duration];
-[PKHandwritingSynthesisLogEntry locale];
-[PKHandwritingSynthesisLogEntry description];
-[PKHandwritingSynthesisLogEntry contextStrokes];
-[PKHandwritingSynthesisLogEntry originalStrokes];
-[PKHandwritingSynthesisLogEntry initWithDebugInfo:];
-[PKHandwritingSynthesisLogEntry initWithLocale:duration:debugInfo:];
-[PKHandwritingSynthesisLogEntry synthesizedStrokes];
```
