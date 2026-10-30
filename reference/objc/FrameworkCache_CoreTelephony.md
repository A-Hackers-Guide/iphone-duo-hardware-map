# `FrameworkCache`

- Image: [`/System/Library/Frameworks/CoreTelephony.framework/CoreTelephony`](../userland/System__Library__Frameworks__CoreTelephony.framework__CoreTelephony.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 1 instance variables, 0 properties, 5 instance methods, 2 class methods

## Instance variables

```
@"NSMutableDictionary" _selectorValueDict;
```

## Class methods

```
+[FrameworkCache getCacheableSelectorForNotification:];
+[FrameworkCache getCachePolicyForSelector:];
```

## Instance methods

```
-[FrameworkCache handleNotification:];
-[FrameworkCache init];
-[FrameworkCache valueForSelector:];
-[FrameworkCache handleValue:forSelector:];
-[FrameworkCache handleDisconnection];
```
