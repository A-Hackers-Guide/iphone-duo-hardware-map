# `_UIHostedWindowHostingHandle`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSSecureCoding`
- 4 instance variables, 4 properties, 6 instance methods, 2 class methods

## Instance variables

```
i _pid;
I _contextID;
{CGAffineTransform="a"d"b"d"c"d"d"d"tx"d"ty"d} _rootLayerTransform;
{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}} _rootLayerFrame;
```

## Properties

```
@property (Ti,R,N,V_pid) pid;
@property (TI,R,N,V_contextID) contextID;
@property (T{CGAffineTransform=dddddd},R,N,V_rootLayerTransform) rootLayerTransform;
@property (T{CGRect={CGPoint=dd}{CGSize=dd}},R,N,V_rootLayerFrame) rootLayerFrame;
```

## Class methods

```
+[_UIHostedWindowHostingHandle supportsSecureCoding];
+[_UIHostedWindowHostingHandle hostedWindowHostingHandleWithContextID:rootLayerTransform:rootLayerFrame:];
```

## Instance methods

```
-[_UIHostedWindowHostingHandle pid];
-[_UIHostedWindowHostingHandle encodeWithCoder:];
-[_UIHostedWindowHostingHandle initWithCoder:];
-[_UIHostedWindowHostingHandle contextID];
-[_UIHostedWindowHostingHandle rootLayerFrame];
-[_UIHostedWindowHostingHandle rootLayerTransform];
```
