# `NSGZipDecoder`

- Image: [`/System/Library/Frameworks/CFNetwork.framework/CFNetwork`](../userland/System__Library__Frameworks__CFNetwork.framework__CFNetwork.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSURLDownloadDecoder`
- 7 instance variables, 4 properties, 8 instance methods, 0 class methods

## Instance variables

```
{?="dst_ptr"*"dst_size"Q"src_ptr"*"src_size"Q"state"^v} _stream;
Q _modificationTime;
@"NSString" _filename;
B _streamInitialized;
B _decodedHeader;
B _finishedInflating;
B _pad;
```

## Properties

```
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[NSGZipDecoder init];
-[NSGZipDecoder dealloc];
-[NSGZipDecoder fileAttributes];
-[NSGZipDecoder decodeData:];
-[NSGZipDecoder decodeDownloadData:dataForkData:resourceForkData:];
-[NSGZipDecoder filenameWithOriginalFilename:];
-[NSGZipDecoder finishDownloadDecoding];
-[NSGZipDecoder isFinishedDecoding];
```
