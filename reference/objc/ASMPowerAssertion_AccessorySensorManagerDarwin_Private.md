# `ASMPowerAssertion`

- Image: [`/System/Library/PrivateFrameworks/AccessorySensorManagerDarwin_Private.framework/AccessorySensorManagerDarwin_Private`](../userland/System__Library__PrivateFrameworks__AccessorySensorManagerDarwin_Private.framework__AccessorySensorManagerDarwin_Private.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 6 instance variables, 0 properties, 6 instance methods, 0 class methods

## Instance variables

```
B _assertionActive;
@"NSString" _assertionName;
I _assertionID;
d _timeout;
@"NSObject<OS_dispatch_source>" _timeoutTimer;
Q _refCount;
```

## Instance methods

```
-[ASMPowerAssertion acquireAssertion];
-[ASMPowerAssertion invalidate];
-[ASMPowerAssertion releaseAssertion];
-[ASMPowerAssertion _resetTimer];
-[ASMPowerAssertion initWithAssertionName:timeout:];
-[ASMPowerAssertion withAssertion:];
```
