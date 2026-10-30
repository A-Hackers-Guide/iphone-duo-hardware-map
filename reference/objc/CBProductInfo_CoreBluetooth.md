# `CBProductInfo`

- Image: [`/System/Library/Frameworks/CoreBluetooth.framework/CoreBluetooth`](../userland/System__Library__Frameworks__CoreBluetooth.framework__CoreBluetooth.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 9 instance variables, 9 properties, 10 instance methods, 1 class methods

## Instance variables

```
S _vendorIDBluetooth;
S _vendorIDUSB;
I _flags;
I _productID;
I _radarComponentID;
@"NSString" _model;
@"NSString" _productName;
@"NSString" _sfSymbolNameCase;
@"NSString" _sfSymbolNameMain;
```

## Properties

```
@property (TI,R,N,V_flags) flags;
@property (T@"NSString",R,C,N,V_model) model;
@property (TI,R,N,V_productID) productID;
@property (T@"NSString",R,C,N,V_productName) productName;
@property (TI,R,N,V_radarComponentID) radarComponentID;
@property (T@"NSString",R,C,N,V_sfSymbolNameCase) sfSymbolNameCase;
@property (T@"NSString",R,C,N,V_sfSymbolNameMain) sfSymbolNameMain;
@property (TS,R,N,V_vendorIDBluetooth) vendorIDBluetooth;
@property (TS,R,N,V_vendorIDUSB) vendorIDUSB;
```

## Class methods

```
+[CBProductInfo productInfoWithProductID:];
```

## Instance methods

```
-[CBProductInfo productID];
-[CBProductInfo model];
-[CBProductInfo flags];
-[CBProductInfo productName];
-[CBProductInfo radarComponentID];
-[CBProductInfo sfSymbolNameMain];
-[CBProductInfo vendorIDBluetooth];
-[CBProductInfo initWithProductInfoPtr:];
-[CBProductInfo sfSymbolNameCase];
-[CBProductInfo vendorIDUSB];
```
