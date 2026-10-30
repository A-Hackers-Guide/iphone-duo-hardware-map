# `LARatchet`

- Image: [`/System/Library/Frameworks/LocalAuthentication.framework/LocalAuthentication`](../userland/System__Library__Frameworks__LocalAuthentication.framework__LocalAuthentication.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 3 instance variables, 1 properties, 8 instance methods, 0 class methods

## Instance variables

```
@"LARatchetManager" _ratchetManager;
@"LAContext" _context;
@"NSString" _identifier;
```

## Properties

```
@property (T@"NSString",R,N,V_identifier) identifier;
```

## Instance methods

```
-[LARatchet identifier];
-[LARatchet removeObserver:];
-[LARatchet addObserver:];
-[LARatchet setContext:];
-[LARatchet initWithIdentifier:];
-[LARatchet cancelWithReason:completion:];
-[LARatchet stateWithCompletion:];
-[LARatchet armWithOptions:completion:];
```
