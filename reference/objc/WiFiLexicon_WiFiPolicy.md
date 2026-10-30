# `WiFiLexicon`

- Image: [`/System/Library/PrivateFrameworks/WiFiPolicy.framework/WiFiPolicy`](../userland/System__Library__PrivateFrameworks__WiFiPolicy.framework__WiFiPolicy.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 6 instance variables, 4 properties, 12 instance methods, 0 class methods

## Instance variables

```
^{_LXLexicon=} _lexiconEnglish;
^{_LXLexicon=} _lexiconUserLocale;
@"NSCharacterSet" _tokenizationCharacterSet;
@"NSCharacterSet" _tokenizationCharacterSetWithoutUpperCase;
@"NSMutableDictionary" _stringCache;
@"NSSet" _unwantedEnglishWords;
```

## Properties

```
@property (T@"NSCharacterSet",&,N,V_tokenizationCharacterSet) tokenizationCharacterSet;
@property (T@"NSCharacterSet",&,N,V_tokenizationCharacterSetWithoutUpperCase) tokenizationCharacterSetWithoutUpperCase;
@property (T@"NSMutableDictionary",&,N,V_stringCache) stringCache;
@property (T@"NSSet",&,N,V_unwantedEnglishWords) unwantedEnglishWords;
```

## Instance methods

```
-[WiFiLexicon init];
-[WiFiLexicon dealloc];
-[WiFiLexicon setStringCache:];
-[WiFiLexicon _tokenizeStringForSpecialCharacters:];
-[WiFiLexicon setTokenizationCharacterSet:];
-[WiFiLexicon setTokenizationCharacterSetWithoutUpperCase:];
-[WiFiLexicon setUnwantedEnglishWords:];
-[WiFiLexicon stringCache];
-[WiFiLexicon stringContainsUnwantedWords:];
-[WiFiLexicon tokenizationCharacterSet];
-[WiFiLexicon tokenizationCharacterSetWithoutUpperCase];
-[WiFiLexicon unwantedEnglishWords];
```
