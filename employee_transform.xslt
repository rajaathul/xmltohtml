<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">

<xsl:template match="/">
  <html>
  <head>
    <title>Employee Details</title>
  </head>
  <body>
    <h1>Employee Details</h1>
    <table border="1">
      <tr>
        <th>ID</th>
        <th>First Name</th>
        <th>Last Name</th>
        <th>DOB</th>
        <th>Gender</th>
        <th>Position</th>
        <th>Salary</th>
        <th>Email</th>
        <th>Phone Number</th>
      </tr>
      <xsl:for-each select="employees/employee">
        <tr>
          <td><xsl:value-of select="@id"/></td>
          <td><xsl:value-of select="personal_details/First_name"/></td>
          <td><xsl:value-of select="personal_details/Last_name"/></td>
          <td><xsl:value-of select="personal_details/dob"/></td>
          <td><xsl:value-of select="personal_details/gender"/></td>
          <td><xsl:value-of select="employee_details/Position"/></td>
          <td><xsl:value-of select="employee_details/salary"/></td>
          <td><xsl:value-of select="contact_details/Email"/></td>
          <td><xsl:value-of select="contact_details/Phone_number"/></td>
        </tr>
      </xsl:for-each>
    </table>
  </body>
  </html>
</xsl:template>

</xsl:stylesheet>
