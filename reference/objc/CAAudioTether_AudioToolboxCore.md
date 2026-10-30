# `CAAudioTether`

- Image: [`/System/Library/PrivateFrameworks/AudioToolboxCore.framework/AudioToolboxCore`](../userland/System__Library__PrivateFrameworks__AudioToolboxCore.framework__AudioToolboxCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSSecureCoding`
- 3 instance variables, 0 properties, 9 instance methods, 1 class methods

## Instance variables

```
q _type;
@"NSUUID" _identifier;
i _pid;
```

## Class methods

```
+[CAAudioTether supportsSecureCoding];
```

## Instance methods

```
-[CAAudioTether identifier];
-[CAAudioTether pid];
-[CAAudioTether type];
-[CAAudioTether encodeWithCoder:];
-[CAAudioTether description];
-[CAAudioTether initWithCoder:];
-[CAAudioTether copyWithZone:];
-[CAAudioTether isEqual:];
-[CAAudioTether initWithType:identifier:pid:];
```
