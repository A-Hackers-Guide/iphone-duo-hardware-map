# `DYCAMetalLayerInfo`

- Image: [`/System/Library/PrivateFrameworks/MTLToolsDeviceSupport.framework/MTLToolsDeviceSupport`](../userland/System__Library__PrivateFrameworks__MTLToolsDeviceSupport.framework__MTLToolsDeviceSupport.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `DYCapturableObject`, `NSSecureCoding`
- 6 instance variables, 12 properties, 11 instance methods, 1 class methods

## Instance variables

```
@"NSString" _displayName;
Q _deviceAddress;
Q _layerAddress;
@"NSString" _name;
Q _layerStreamRef;
{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}} _frame;
```

## Properties

```
@property (TQ,R,N,V_deviceAddress) deviceAddress;
@property (TQ,R,N,V_layerAddress) layerAddress;
@property (T{CGRect={CGPoint=dd}{CGSize=dd}},R,N,V_frame) frame;
@property (T@"NSString",R,C,N,V_name) name;
@property (TQ,R,N,V_layerStreamRef) layerStreamRef;
@property (T@"NSString",R,N) capturableObjectType;
@property (T@"NSString",R,N,V_displayName) displayName;
@property (TQ,R,N) streamRef;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[DYCAMetalLayerInfo supportsSecureCoding];
```

## Instance methods

```
-[DYCAMetalLayerInfo displayName];
-[DYCAMetalLayerInfo layerAddress];
-[DYCAMetalLayerInfo encodeWithCoder:];
-[DYCAMetalLayerInfo initWithCoder:];
-[DYCAMetalLayerInfo isEqual:];
-[DYCAMetalLayerInfo name];
-[DYCAMetalLayerInfo frame];
-[DYCAMetalLayerInfo deviceAddress];
-[DYCAMetalLayerInfo streamRef];
-[DYCAMetalLayerInfo layerStreamRef];
-[DYCAMetalLayerInfo capturableObjectType];
```
