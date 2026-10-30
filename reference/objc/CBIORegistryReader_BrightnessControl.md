# `CBIORegistryReader`

- Image: [`/System/Library/PrivateFrameworks/BrightnessControl.framework/BrightnessControl`](../userland/System__Library__PrivateFrameworks__BrightnessControl.framework__BrightnessControl.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `CBIORegInterface`
- 3 instance variables, 5 properties, 7 instance methods, 4 class methods

## Instance variables

```
I _options;
[128c] _plane;
I _service;
```

## Properties

```
@property (TI,R,V_service) service;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[CBIORegistryReader readerWithService:];
+[CBIORegistryReader readerWithService:andOptions:];
+[CBIORegistryReader readerWithService:andPlane:];
+[CBIORegistryReader readerWithService:andPlane:andOptions:];
```

## Instance methods

```
-[CBIORegistryReader dealloc];
-[CBIORegistryReader service];
-[CBIORegistryReader initWithService:];
-[CBIORegistryReader copyProperty:];
-[CBIORegistryReader initWithService:andOptions:];
-[CBIORegistryReader initWithService:andPlane:];
-[CBIORegistryReader initWithService:andPlane:andOptions:];
```
