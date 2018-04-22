define(['minor'], function (minor) {

  function main() {
    console.log('medior.main shows minor.name')
    console.debug(minor.name)
  }

  return {
    main: main
  }

});
