# `LACOwnerInfos`

- Image: [`/System/Library/PrivateFrameworks/LocalAuthenticationCore.framework/LocalAuthenticationCore`](../userland/System__Library__PrivateFrameworks__LocalAuthenticationCore.framework__LocalAuthenticationCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 2 instance variables, 2 properties, 7 instance methods, 0 class methods

## Instance variables

```
@"NSMutableArray" _allInfos;
@"<LACContextExternalizing>" _context;
```

## Properties

```
@property (T@"NSArray",R,N) allInfos;
@property (T@"<LACContextExternalizing>",R,W,N,V_context) context;
```

## Instance methods

```
-[LACOwnerInfos cleanup];
-[LACOwnerInfos description];
-[LACOwnerInfos context];
-[LACOwnerInfos addInfo:];
-[LACOwnerInfos allInfos];
-[LACOwnerInfos initWithInfo:context:];
-[LACOwnerInfos numberOfOwnersOtherThanPid:];
```
