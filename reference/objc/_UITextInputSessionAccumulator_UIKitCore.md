# `_UITextInputSessionAccumulator`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`
- 5 instance variables, 4 properties, 14 instance methods, 2 class methods

## Instance variables

```
[9Q] _values;
@"NSString" _name;
q _type;
@? _block;
{_NSRange="location"Q"length"Q} _depthRange;
```

## Properties

```
@property (T@"NSString",C,N,V_name) name;
@property (Tq,N,V_type) type;
@property (T{_NSRange=QQ},N,V_depthRange) depthRange;
@property (T@?,R,N,V_block) block;
```

## Class methods

```
+[_UITextInputSessionAccumulator accumulatorWithName:type:depth:block:];
+[_UITextInputSessionAccumulator accumulatorWithName:type:depthRange:block:];
```

## Instance methods

```
-[_UITextInputSessionAccumulator depthRange];
-[_UITextInputSessionAccumulator block];
-[_UITextInputSessionAccumulator _increaseWithCount:source:];
-[_UITextInputSessionAccumulator reset];
-[_UITextInputSessionAccumulator increaseWithActions:];
-[_UITextInputSessionAccumulator _increaseWithActions:];
-[_UITextInputSessionAccumulator enumerateAnalytics:];
-[_UITextInputSessionAccumulator setType:];
-[_UITextInputSessionAccumulator type];
-[_UITextInputSessionAccumulator description];
-[_UITextInputSessionAccumulator setName:];
-[_UITextInputSessionAccumulator copyWithZone:];
-[_UITextInputSessionAccumulator setDepthRange:];
-[_UITextInputSessionAccumulator name];
```
