# `DetachedCertificatesLookup`

- Image: [`/System/Library/Frameworks/Security.framework/Security`](../userland/System__Library__Frameworks__Security.framework__Security.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 0 instance variables, 0 properties, 5 instance methods, 2 class methods

## Class methods

```
+[DetachedCertificatesLookup loadCertificatesFileMatching:skid:];
+[DetachedCertificatesLookup searchInsideOutForFile:skid:];
```

## Instance methods

```
-[DetachedCertificatesLookup extractSKIDFromCMSData:error:];
-[DetachedCertificatesLookup lookupCertificatesForExecutable:cmsData:error:];
-[DetachedCertificatesLookup lookupCertificatesForExecutable:skid:error:];
-[DetachedCertificatesLookup lookupDetachedCertificatesFileForExecutable:cmsData:error:];
-[DetachedCertificatesLookup lookupDetachedCertificatesFileForExecutable:skid:error:];
```
