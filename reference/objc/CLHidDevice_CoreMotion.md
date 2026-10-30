# `CLHidDevice`

- Image: [`/System/Library/Frameworks/CoreMotion.framework/CoreMotion`](../userland/System__Library__Frameworks__CoreMotion.framework__CoreMotion.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 2 instance variables, 2 properties, 7 instance methods, 0 class methods

## Instance variables

```
@"NSDictionary" _matching;
@"HIDDevice" _hidDevice;
```

## Properties

```
@property (T@"HIDDevice",&,N,V_hidDevice) hidDevice;
@property (T@"NSDictionary",&,N,V_matching) matching;
```

## Instance methods

```
-[CLHidDevice setMatching:];
-[CLHidDevice dealloc];
-[CLHidDevice matching];
-[CLHidDevice initWithHidDevice:matchingDict:];
-[CLHidDevice hidDevice];
-[CLHidDevice setHidDevice:];
-[CLHidDevice setReport:payload:length:];
```
