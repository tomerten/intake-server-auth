intake-server-auth
==================

This plugin allows to use authorization for an [intake-server](https://github.com/intake/intake) over an NGINX reverse proxy. 

It uses an external json file to keep track of which source is visible (still TODO) and accessible to which user.

Below is an example of such an external JSON file.

```json
{
  "source_1": ["user1", "user2"],
  "source_2": ["user2"]
}
```

with a corresponding catalog yaml file:

```yaml
sources:
  source_1:
    driver: python
    args:
      urlpath: 'catalogdir/source_1'
    metadata:
      plots:
        beta:
          x: S
          y: [BETX,BETY,DX]
        phase:
          x: S
          y: [MUX, MUY]
  source_2:
    driver: custom_source_container
    args:
      urlpath: 'catalogdir/source_2'
    metadata:
      plots:
        beta:
          x: S
          y: [BETX,BETY,DX]
        phase:
          x: S
          y: [MUX, MUY]

```


