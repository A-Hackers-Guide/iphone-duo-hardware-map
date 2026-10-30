# `BLSDiagnosticPresentationDateSpecifier`

- Image: [`/System/Library/PrivateFrameworks/BacklightServices.framework/BacklightServices`](../userland/System__Library__PrivateFrameworks__BacklightServices.framework__BacklightServices.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `BLSPresentationDateSpecifying`, `NSSecureCoding`, `BSXPCCoding`
- 2 instance variables, 6 properties, 13 instance methods, 2 class methods

## Instance variables

```
@"NSArray" _specifiers;
@"NSDate" _presentationDate;
```

## Properties

```
@property (T@"NSDate",R,N,V_presentationDate) presentationDate;
@property (T@"NSArray",R,N) specifiers;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[BLSDiagnosticPresentationDateSpecifier supportsSecureCoding];
+[BLSDiagnosticPresentationDateSpecifier createWithSpecifier:];
```

## Instance methods

```
-[BLSDiagnosticPresentationDateSpecifier bls_loggingString];
-[BLSDiagnosticPresentationDateSpecifier bls_shortLoggingString];
-[BLSDiagnosticPresentationDateSpecifier initWithXPCDictionary:];
-[BLSDiagnosticPresentationDateSpecifier encodeWithXPCDictionary:];
-[BLSDiagnosticPresentationDateSpecifier encodeWithCoder:];
-[BLSDiagnosticPresentationDateSpecifier hash];
-[BLSDiagnosticPresentationDateSpecifier description];
-[BLSDiagnosticPresentationDateSpecifier presentationDate];
-[BLSDiagnosticPresentationDateSpecifier initWithCoder:];
-[BLSDiagnosticPresentationDateSpecifier copyWithZone:];
-[BLSDiagnosticPresentationDateSpecifier isEqual:];
-[BLSDiagnosticPresentationDateSpecifier specifiers];
-[BLSDiagnosticPresentationDateSpecifier initWithPresentationDate:specifiers:];
```
