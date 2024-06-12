// test6

// added line 
// added one more line

module.exports = function searchProducts () {
  return (req: Request, res: Response, next: NextFunction) => {
    // TODO: fix it
    let criteria: any = req.query.q === 'undefined' ? '' : req.query.q ?? ''
    // TODO: fix it
    criteria = (criteria.length <= 200) ? criteria : criteria.substring(0, 200)
    // TODO: fix it
    models.sequelize.query("SELECT * FROM Products WHERE ((name LIKE '%"+criteria+"%' OR description LIKE '%"+criteria+"%') AND deletedAt IS NULL) ORDER BY name")
      .then(([products]: any) => {
        const dataString = JSON.stringify(products)
        for (let i = 0; i < products.length; i++) {
          products[i].name = req.__(products[i].name)
          products[i].description = req.__(products[i].description)
        }
        res.json(utils.queryResultToJson(products))
      }).catch((error: ErrorWithParent) => {
        next(error.parent)
      })
  }
}
