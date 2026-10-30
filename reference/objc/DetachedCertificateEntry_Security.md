# `DetachedCertificateEntry`

- Image: [`/System/Library/Frameworks/Security.framework/Security`](../userland/System__Library__Frameworks__Security.framework__Security.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 3 instance variables, 3 properties, 6 instance methods, 0 class methods

## Instance variables

```
@"NSData" _skid;
@"NSData" _certificate;
@"NSData" _akid;
```

## Properties

```
@property (T@"NSData",R,N,V_skid) skid;
@property (T@"NSData",R,N,V_certificate) certificate;
@property (T@"NSData",R,N,V_akid) akid;
```

## Instance methods

```
-[DetachedCertificateEntry hash];
-[DetachedCertificateEntry certificate];
-[DetachedCertificateEntry isEqual:];
-[DetachedCertificateEntry akid];
-[DetachedCertificateEntry initWithSKID:certificate:akid:];
-[DetachedCertificateEntry skid];
```
