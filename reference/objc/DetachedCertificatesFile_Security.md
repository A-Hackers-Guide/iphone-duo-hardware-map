# `DetachedCertificatesFile`

- Image: [`/System/Library/Frameworks/Security.framework/Security`](../userland/System__Library__Frameworks__Security.framework__Security.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 8 instance variables, 8 properties, 34 instance methods, 4 class methods

## Instance variables

```
Q _version;
Q _compatibilityVersion;
@"NSMutableArray" _leafCertificates;
@"NSMutableArray" _intermediateCertificates;
@"NSMutableArray" _rootCertificates;
@"NSMutableDictionary" _leafSKIDMap;
@"NSMutableDictionary" _intermediateSKIDMap;
@"NSMutableDictionary" _rootSKIDMap;
```

## Properties

```
@property (TQ,N,V_version) version;
@property (TQ,N,V_compatibilityVersion) compatibilityVersion;
@property (T@"NSMutableArray",&,N,V_leafCertificates) leafCertificates;
@property (T@"NSMutableArray",&,N,V_intermediateCertificates) intermediateCertificates;
@property (T@"NSMutableArray",&,N,V_rootCertificates) rootCertificates;
@property (T@"NSMutableDictionary",&,N,V_leafSKIDMap) leafSKIDMap;
@property (T@"NSMutableDictionary",&,N,V_intermediateSKIDMap) intermediateSKIDMap;
@property (T@"NSMutableDictionary",&,N,V_rootSKIDMap) rootSKIDMap;
```

## Class methods

```
+[DetachedCertificatesFile loadFromPath:error:];
+[DetachedCertificatesFile parseCertificateEntry:certificate:error:];
+[DetachedCertificatesFile parseCertificateSequence:certificates:error:];
+[DetachedCertificatesFile parseFromData:error:];
```

## Instance methods

```
-[DetachedCertificatesFile setCompatibilityVersion:];
-[DetachedCertificatesFile init];
-[DetachedCertificatesFile compatibilityVersion];
-[DetachedCertificatesFile version];
-[DetachedCertificatesFile hash];
-[DetachedCertificatesFile setVersion:];
-[DetachedCertificatesFile isEqual:];
-[DetachedCertificatesFile rebuildSKIDMaps];
-[DetachedCertificatesFile setLeafSKIDMap:];
-[DetachedCertificatesFile setRootSKIDMap:];
-[DetachedCertificatesFile addCertificateChainWithLeaf:intermediate:error:];
-[DetachedCertificatesFile addCertificateChainWithLeaf:intermediate:root:error:];
-[DetachedCertificatesFile addCertificateChainsWithLeaves:parents:error:];
-[DetachedCertificatesFile derEncodedSize];
-[DetachedCertificatesFile encodeCertificateEntry:der:der_end:];
-[DetachedCertificatesFile extractAKIDFromCertificate:certificateName:error:];
-[DetachedCertificatesFile extractSKIDFromCertificate:certificateName:error:];
-[DetachedCertificatesFile intermediateCertificates];
-[DetachedCertificatesFile intermediateSKIDMap];
-[DetachedCertificatesFile leafCertificates];
-[DetachedCertificatesFile leafSKIDMap];
-[DetachedCertificatesFile lookupCertificateChainForSKID:error:];
-[DetachedCertificatesFile mergeWithFile:error:];
-[DetachedCertificatesFile removeRootCertificates];
-[DetachedCertificatesFile rootCertificates];
-[DetachedCertificatesFile rootSKIDMap];
-[DetachedCertificatesFile setIntermediateCertificates:];
-[DetachedCertificatesFile setIntermediateSKIDMap:];
-[DetachedCertificatesFile setLeafCertificates:];
-[DetachedCertificatesFile setRootCertificates:];
-[DetachedCertificatesFile sizeOfCertificateEntry:];
-[DetachedCertificatesFile sortCertificateArrays];
-[DetachedCertificatesFile writeToData:];
-[DetachedCertificatesFile writeToPath:error:];
```
