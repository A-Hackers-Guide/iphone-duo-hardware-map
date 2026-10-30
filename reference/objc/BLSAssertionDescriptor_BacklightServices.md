# `BLSAssertionDescriptor`

- Image: [`/System/Library/PrivateFrameworks/BacklightServices.framework/BacklightServices`](../userland/System__Library__PrivateFrameworks__BacklightServices.framework__BacklightServices.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`, `NSSecureCoding`, `BSXPCCoding`
- 4 instance variables, 6 properties, 15 instance methods, 2 class methods

## Instance variables

```
{os_unfair_lock_s="_os_unfair_lock_opaque"I} _lock;
@"NSArray" _lock_displays;
@"NSString" _explanation;
@"NSArray" _attributes;
```

## Properties

```
@property (T@"NSString",R,C,N,V_explanation) explanation;
@property (T@"NSArray",R,C,N,V_attributes) attributes;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[BLSAssertionDescriptor supportsSecureCoding];
+[BLSAssertionDescriptor setHighLuminanceSupportedByCoreBrightness:];
```

## Instance methods

```
-[BLSAssertionDescriptor explanation];
-[BLSAssertionDescriptor initWithXPCDictionary:];
-[BLSAssertionDescriptor encodeWithXPCDictionary:];
-[BLSAssertionDescriptor initWithExplanation:attributes:];
-[BLSAssertionDescriptor encodeWithCoder:];
-[BLSAssertionDescriptor hash];
-[BLSAssertionDescriptor description];
-[BLSAssertionDescriptor initWithCoder:];
-[BLSAssertionDescriptor attributes];
-[BLSAssertionDescriptor copyWithZone:];
-[BLSAssertionDescriptor isEqual:];
-[BLSAssertionDescriptor checkEntitlementSourceForRequiredEntitlements:error:];
-[BLSAssertionDescriptor attributeOfClass:];
-[BLSAssertionDescriptor attributesOfClasses:];
-[BLSAssertionDescriptor canAcquireForDisplay:];
```
