# `LADomainState`

- Image: [`/System/Library/Frameworks/LocalAuthentication.framework/LocalAuthentication`](../userland/System__Library__Frameworks__LocalAuthentication.framework__LocalAuthentication.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 3 instance variables, 3 properties, 6 instance methods, 0 class methods

## Instance variables

```
@"NSData" _stateHash;
@"LADomainStateBiometry" _biometry;
@"LADomainStateCompanion" _companion;
```

## Properties

```
@property (T@"LADomainStateBiometry",R,N,V_biometry) biometry;
@property (T@"LADomainStateCompanion",R,N,V_companion) companion;
@property (T@"NSData",R,N) stateHash;
```

## Instance methods

```
-[LADomainState biometry];
-[LADomainState companion];
-[LADomainState stateHash];
-[LADomainState initWithResult:];
-[LADomainState description];
-[LADomainState _resolveCombinedStateHash];
```
