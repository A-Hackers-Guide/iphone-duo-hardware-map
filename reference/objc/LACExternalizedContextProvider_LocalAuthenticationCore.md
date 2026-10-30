# `LACExternalizedContextProvider`

- Image: [`/System/Library/PrivateFrameworks/LocalAuthenticationCore.framework/LocalAuthenticationCore`](../userland/System__Library__PrivateFrameworks__LocalAuthenticationCore.framework__LocalAuthenticationCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 3 instance variables, 3 properties, 10 instance methods, 0 class methods

## Instance variables

```
@"<LACContextExternalizing>" _externalizer;
@"NSData" _cachedExternalizedContext;
@"<LACContextExternalizationObserving>" _externalizationObserver;
```

## Properties

```
@property (T@"NSData",&,V_cachedExternalizedContext) cachedExternalizedContext;
@property (T@"NSData",R,N) externalizedContext;
@property (T@"<LACContextExternalizationObserving>",W,N,V_externalizationObserver) externalizationObserver;
```

## Instance methods

```
-[LACExternalizedContextProvider externalizationObserver];
-[LACExternalizedContextProvider setExternalizationObserver:];
-[LACExternalizedContextProvider initWithExternalizedContext:];
-[LACExternalizedContextProvider cachedExternalizedContext];
-[LACExternalizedContextProvider externalizedContext];
-[LACExternalizedContextProvider invalidateBecauseOfInvalidConnection:];
-[LACExternalizedContextProvider setCachedExternalizedContext:];
-[LACExternalizedContextProvider externalizedContextWithError:];
-[LACExternalizedContextProvider externalizedContextWithReply:];
-[LACExternalizedContextProvider initWithExternalizer:];
```
