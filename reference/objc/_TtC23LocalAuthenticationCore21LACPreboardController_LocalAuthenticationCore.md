# `_TtC23LocalAuthenticationCore21LACPreboardController`

- Image: [`/System/Library/PrivateFrameworks/LocalAuthenticationCore.framework/LocalAuthenticationCore`](../userland/System__Library__PrivateFrameworks__LocalAuthenticationCore.framework__LocalAuthenticationCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `LACPreboardControlling`
- 9 instance variables, 3 properties, 8 instance methods, 0 class methods

## Instance variables

```
LocalAuthenticationCore.LACPreboardACMContextProviderFactory contextProviderFactory;
LocalAuthenticationCore.LACPreboardLaunching launcher;
LocalAuthenticationCore.LACPreboardPasscodeVerifying passcodeVerifier;
LocalAuthenticationCore.LACPreboardStorageType storage;
LocalAuthenticationCore.LACPreboardUPPManaging uppManager;
LocalAuthenticationCore.LACPreboardUseCaseProviding useCaseProvider;
LocalAuthenticationCore.LACACMContextProviding ?? $__lazy_storage_$_contextProvider;
_$sSaySo8NSNumberCGSg batchOptionsResult;
DispatchQueue $__lazy_storage_$_syncDispatchQueue;
```

## Properties

```
@property (T@"NSArray",N,R) batchOptions;
@property (TB,N,R) isRequired;
@property (Tq,N,R) useCase;
```

## Instance methods

```
-[_TtC23LocalAuthenticationCore21LACPreboardController useCase];
-[_TtC23LocalAuthenticationCore21LACPreboardController init];
-[_TtC23LocalAuthenticationCore21LACPreboardController isRequired];
-[_TtC23LocalAuthenticationCore21LACPreboardController batchOptions];
-[_TtC23LocalAuthenticationCore21LACPreboardController enableCurrentUseCaseWithSecurePasscode:completion:];
-[_TtC23LocalAuthenticationCore21LACPreboardController launchPreboardWithCompletion:];
-[_TtC23LocalAuthenticationCore21LACPreboardController terminateWithCompletion:];
-[_TtC23LocalAuthenticationCore21LACPreboardController uppTeamName];
```
