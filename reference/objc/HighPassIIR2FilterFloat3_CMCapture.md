# `HighPassIIR2FilterFloat3`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 4 instance variables, 1 properties, 4 instance methods, 0 class methods

## Instance variables

```
_lowPassBuffer1;
_lowPassBuffer2;
B _isFilterInitialized;
_filteredValue;
```

## Properties

```
@property (T,R,N,V_filteredValue) filteredValue;
```

## Instance methods

```
-[HighPassIIR2FilterFloat3 init];
-[HighPassIIR2FilterFloat3 reset];
-[HighPassIIR2FilterFloat3 filteredValue];
-[HighPassIIR2FilterFloat3 updateValue:withPole:];
```
