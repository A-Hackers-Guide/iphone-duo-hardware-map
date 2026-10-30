# `LARightContextHandler`

- Image: [`/System/Library/Frameworks/LocalAuthentication.framework/LocalAuthentication`](../userland/System__Library__Frameworks__LocalAuthentication.framework__LocalAuthentication.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `LACContextObserver`
- 2 instance variables, 6 properties, 7 instance methods, 0 class methods

## Instance variables

```
@"<LARightContextHandlerDelegate>" _delegate;
@"LAContext" _context;
```

## Properties

```
@property (T@"<LARightContextHandlerDelegate>",W,N,V_delegate) delegate;
@property (T@"LAContext",&,N,V_context) context;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[LARightContextHandler initWithDelegate:];
-[LARightContextHandler init];
-[LARightContextHandler setDelegate:];
-[LARightContextHandler setContext:];
-[LARightContextHandler delegate];
-[LARightContextHandler context];
-[LARightContextHandler contextDidBecomeInvalid:];
```
