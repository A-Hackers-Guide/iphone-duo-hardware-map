# `MTLAirEntry`

- Image: [`/System/Library/Frameworks/Metal.framework/Metal`](../userland/System__Library__Frameworks__Metal.framework__Metal.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 5 instance variables, 5 properties, 9 instance methods, 0 class methods

## Instance variables

```
@"NSObject<OS_dispatch_data>" _data;
@"NSObject<OS_dispatch_data>" _bitcode;
@"NSObject<OS_dispatch_data>" _airScript;
{?="key"[32C]} _hash;
@"NSArray" _linkedBitcodes;
```

## Properties

```
@property (T@"NSObject<OS_dispatch_data>",R,V_data) data;
@property (T@"NSObject<OS_dispatch_data>",R,V_airScript) airScript;
@property (T@"NSObject<OS_dispatch_data>",R,V_bitcode) bitcode;
@property (T^{?=[32C]},R) hash;
@property (T@"NSArray",&,V_linkedBitcodes) linkedBitcodes;
```

## Instance methods

```
-[MTLAirEntry airScript];
-[MTLAirEntry linkedBitcodes];
-[MTLAirEntry data];
-[MTLAirEntry dealloc];
-[MTLAirEntry initWithData:bitcode:airScript:hash:];
-[MTLAirEntry bitcode];
-[MTLAirEntry hash];
-[MTLAirEntry initWithData:];
-[MTLAirEntry setLinkedBitcodes:];
```
