# `LADomainStateCompanion`

- Image: [`/System/Library/Frameworks/LocalAuthentication.framework/LocalAuthentication`](../userland/System__Library__Frameworks__LocalAuthentication.framework__LocalAuthentication.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 3 instance variables, 2 properties, 6 instance methods, 0 class methods

## Instance variables

```
@"NSMutableSet" _availableCompanions;
@"NSData" _stateHash;
@"NSMutableDictionary" _stateHashForCompanionType;
```

## Properties

```
@property (T@"NSSet",R,N) availableCompanionTypes;
@property (T@"NSData",R,N) stateHash;
```

## Instance methods

```
-[LADomainStateCompanion stateHash];
-[LADomainStateCompanion initWithResult:];
-[LADomainStateCompanion description];
-[LADomainStateCompanion availableCompanionTypes];
-[LADomainStateCompanion _resolveCombinedStateHash];
-[LADomainStateCompanion stateHashForCompanionType:];
```
