# `LACDomainStateProvider`

- Image: [`/System/Library/PrivateFrameworks/LocalAuthenticationCore.framework/LocalAuthenticationCore`](../userland/System__Library__PrivateFrameworks__LocalAuthenticationCore.framework__LocalAuthenticationCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `LACDomainStateProviding`
- 1 instance variables, 4 properties, 3 instance methods, 0 class methods

## Instance variables

```
@"NSArray" _providers;
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
-[LACDomainStateProvider _domainStateWithProviders:request:partialResult:completion:];
-[LACDomainStateProvider domainStateForRequest:completion:];
-[LACDomainStateProvider initWithProviders:];
```
