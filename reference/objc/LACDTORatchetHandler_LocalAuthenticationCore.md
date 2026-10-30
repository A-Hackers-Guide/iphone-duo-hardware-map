# `LACDTORatchetHandler`

- Image: [`/System/Library/PrivateFrameworks/LocalAuthenticationCore.framework/LocalAuthenticationCore`](../userland/System__Library__PrivateFrameworks__LocalAuthenticationCore.framework__LocalAuthenticationCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `LACDTORatchetHandler`, `LACDTORatchetStateProvider`
- 2 instance variables, 4 properties, 7 instance methods, 0 class methods

## Instance variables

```
@"<LACRemoteContextProviding>" _contextProvider;
@"<LACDTORatchetSEPInterface>" _sep;
```

## Properties

```
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[LACDTORatchetHandler resetRatchetWithReason:completion:];
-[LACDTORatchetHandler _ratchetStatusWithCompletion:];
-[LACDTORatchetHandler _resetRatchetWithCompletion:];
-[LACDTORatchetHandler initWithContextProvider:sep:];
-[LACDTORatchetHandler ratchetStateCompositeWithCompletion:];
-[LACDTORatchetHandler ratchetStateWithCompletion:];
-[LACDTORatchetHandler restartRatchetWithIdentifier:];
```
